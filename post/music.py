from pymongo import MongoClient
import os
import pretty_midi
import numpy as np


def get_midi_collection():
    client = MongoClient(connect=False)
    return client.free_midi.midi


def get_genre_collection():
    client = MongoClient(connect=False)
    return client.free_midi.genres


def get_classical_collection():
    client = MongoClient(connect=False)
    return client.classical_midi.midi


def get_jazz_midkar_collection():
    client = MongoClient(connect=False)
    return client.jazz_midikar.midi


def get_jazz_collection():
    client = MongoClient(connect=False)
    return client.jazz_midi.midi


def get_classical_composer_collection():
    client = MongoClient(connect=False)
    return client.classical_midi.performers


def merge_all_sparse_matrices():
    midi_collection = get_midi_collection()
    genre_collection = get_genre_collection()

    root_dir = 'E:/midi_matrix/one_instr/'
    time_step = 64
    valid_range = (24, 108)

    for genre in genre_collection.find({'DatasetGenerated': False}):
        save_dir = 'd:/data/' + genre['Name']

        train_file_path = save_dir + '/train.npz'
        test_file_path = save_dir + '/test.npz'

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        print(genre['Name'])
        whole_length = genre['ValidPiecesNum']

        train_length = int(whole_length * 0.9)
        test_length = whole_length - train_length

        train_shape = np.array([train_length, time_step, valid_range[1]-valid_range[0]])
        test_shape = np.array([test_length, time_step, valid_range[1]-valid_range[0]])

        processed = 0
        last_piece_num = 0
        whole_num = midi_collection.count({'Genre': genre['Name']})

        non_zeros_train = []
        non_zeros_test = []

        for midi in midi_collection.find({'Genre': genre['Name']}, no_cursor_timeout=True):

            path = root_dir + genre['Name'] + '/' + midi['md5'] + '.npz'
            valid_pieces_num = midi['ValidPiecesNum']

            f = np.load(path)
            matrix = f['arr_0'].copy()
            for data in matrix:
                try:
                    data = data.tolist()

                    if data[0] < valid_pieces_num:
                        piece_order = last_piece_num + data[0]

                        if piece_order < train_length:
                            non_zeros_train.append([piece_order, data[1], data[2]])
                        else:
                            non_zeros_test.append([piece_order - train_length, data[1], data[2]])
                except:
                    print(path)

            last_piece_num += valid_pieces_num
            processed += 1

            print('\tProgress: {:.2%}\n'.format(processed / whole_num))

        print(last_piece_num, whole_length)
        non_zeros_train, non_zeros_test = np.array(non_zeros_train), np.array(non_zeros_test)

        np.savez_compressed(train_file_path, nonzeros=non_zeros_train, shape=train_shape)
        np.savez_compressed(test_file_path, nonzeros=non_zeros_test, shape=test_shape)

        genre_collection.update_one({'_id': genre['_id']}, {'$set': {'DatasetGenerated': True,
                                                                     'TrainPieces': train_length,
                                                                     'TestPieces': test_length}})


def merge_classical():
    midi_collection = get_classical_collection()
    genre_collection = get_genre_collection()

    root_dir = 'E:/classical_midi/npy_files'
    time_step = 64
    valid_range = (24, 108)

    genre = genre_collection.find_one({'Name': 'classical'})

    save_dir = 'd:/data/' + genre['Name']

    train_file_path = save_dir + '/train.npz'
    test_file_path = save_dir + '/test.npz'

    whole_length = genre['ValidPiecesNum']

    train_length = int(whole_length * 0.9)
    test_length = whole_length - train_length

    train_shape = np.array([train_length, time_step, valid_range[1]-valid_range[0]])
    test_shape = np.array([test_length, time_step, valid_range[1]-valid_range[0]])

    processed = 0
    last_piece_num = 0
    whole_num = genre['FilesNum']

    non_zeros_train = []
    non_zeros_test = []

    for midi in midi_collection.find({}, no_cursor_timeout=True):
        path = root_dir + '/' + midi['md5'] + '.npz'
        valid_pieces_num = midi['ValidPiecesNum']

        f = np.load(path)
        matrix = f['arr_0'].copy()
        for data in matrix:
            try:
                data = data.tolist()

                if data[0] < valid_pieces_num:
                    piece_order = last_piece_num + data[0]

                    if piece_order < train_length:
                        non_zeros_train.append([piece_order, data[1], data[2]])
                    else:
                        non_zeros_test.append([piece_order - train_length, data[1], data[2]])
            except:
                print(path)

        last_piece_num += valid_pieces_num
        processed += 1

        print('\tProgress: {:.2%}\n'.format(processed / whole_num))

    print(last_piece_num, whole_length)
    non_zeros_train, non_zeros_test = np.array(non_zeros_train), np.array(non_zeros_test)

    np.savez_compressed(train_file_path, nonzeros=non_zeros_train, shape=train_shape)
    np.savez_compressed(test_file_path, nonzeros=non_zeros_test, shape=test_shape)


def merge_jazz():
    midi_collection = get_midi_collection()
    jazz_collection = get_jazz_collection()
    jazz_midkar_collection = get_jazz_midkar_collection()
    genre_collection = get_genre_collection()

    extra_dir1 = 'E:/jazz_midi/npy_files'
    extra_dir2 = 'E:/jazz_midkar/npy_files'
    root_dir = 'E:/midi_matrix/one_instr/jazz'

    time_step = 64
    valid_range = (24, 108)

    genre = genre_collection.find_one({'Name': 'jazz'})

    save_dir = 'd:/data/' + genre['Name']

    train_file_path = save_dir + '/train.npz'
    test_file_path = save_dir + '/test.npz'

    train_pieces_dict = genre['TrainPieces']
    test_pieces_dict = genre['TestPieces']
    valid_pieces_dict = genre['ValidPiecesNum']
    files_num_dict = genre['FilesNum']

    train_shape = np.array([train_pieces_dict['whole'], time_step, valid_range[1]-valid_range[0]])
    test_shape = np.array([test_pieces_dict['whole'], time_step, valid_range[1]-valid_range[0]])

    processed = 0
    last_piece_num = 0
    whole_length = files_num_dict['first']

    non_zeros_train = []
    non_zeros_test = []

    for midi in midi_collection.find({'Genre': 'jazz'}, no_cursor_timeout=True):
        path = root_dir + '/' + midi['md5'] + '.npz'
        valid_pieces_num = midi['ValidPiecesNum']

        f = np.load(path)
        matrix = f['arr_0'].copy()
        for data in matrix:
            try:
                data = data.tolist()

                if data[0] < valid_pieces_num:
                    piece_order = last_piece_num + data[0]

                    if piece_order < train_pieces_dict['first']:
                        non_zeros_train.append([piece_order, data[1], data[2]])
                    else:
                        non_zeros_test.append([piece_order - train_pieces_dict['first'], data[1], data[2]])
            except:
                print(path)

        last_piece_num += valid_pieces_num
        processed += 1

        print('\tFirst part Progress: {:.2%}\n'.format(processed / whole_length))
    print(last_piece_num, valid_pieces_dict['first'])

    processed = 0
    last_piece_num = 0
    whole_length = files_num_dict['second']

    for midi in jazz_collection.find({}, no_cursor_timeout=True):
        path = extra_dir1 + '/' + midi['md5'] + '.npz'
        valid_pieces_num = midi['ValidPiecesNum']

        print(valid_pieces_num)

        f = np.load(path)
        matrix = f['arr_0'].copy()
        for data in matrix:
            try:
                data = data.tolist()

                if data[0] < valid_pieces_num:
                    piece_order = last_piece_num + data[0]

                    if piece_order < train_pieces_dict['second']:
                        # print(piece_order + old_train_length)
                        non_zeros_train.append([piece_order + train_pieces_dict['first'], data[1], data[2]])
                    else:
                        non_zeros_test.append([piece_order - train_pieces_dict['second'] + test_pieces_dict['first'], data[1], data[2]])
            except:
                print(path)

        last_piece_num += valid_pieces_num
        processed += 1

        print('\tSecond part Progress: {:.2%}\n'.format(processed / whole_length))

    print(last_piece_num, valid_pieces_dict['second'])

    processed = 0
    last_piece_num = 0
    whole_length = files_num_dict['third']

    for midi in jazz_midkar_collection.find({}, no_cursor_timeout=True):
        path = extra_dir2 + '/' + midi['md5'] + '.npz'
        valid_pieces_num = midi['ValidPiecesNum']

        print(valid_pieces_num)

        f = np.load(path)
        matrix = f['arr_0'].copy()
        for data in matrix:
            try:
                data = data.tolist()

                if data[0] < valid_pieces_num:
                    piece_order = last_piece_num + data[0]

                    if piece_order < train_pieces_dict['third']:
                        # print(piece_order + old_train_length)
                        non_zeros_train.append([piece_order + train_pieces_dict['first'] + train_pieces_dict['second'], data[1], data[2]])
                    else:
                        non_zeros_test.append([piece_order - train_pieces_dict['third'] + test_pieces_dict['first']
                                                  + test_pieces_dict['second'], data[1], data[2]])
            except:
                print(path)

        last_piece_num += valid_pieces_num
        processed += 1

        print('\tThird part Progress: {:.2%}\n'.format(processed / whole_length))

    print(last_piece_num, valid_pieces_dict['third'])
    non_zeros_train, non_zeros_test = np.array(non_zeros_train), np.array(non_zeros_test)

    np.savez_compressed(train_file_path, nonzeros=non_zeros_train, shape=train_shape)
    np.savez_compressed(test_file_path, nonzeros=non_zeros_test, shape=test_shape)


def build_extra_tensor():
    import math
    midi_collection = get_jazz_collection()
    root_dir = 'E:/jazz_midkar/scaled'
    npy_file_root_dir = 'E:/jazz_midkar/npy_files'
    for midi in midi_collection.find({'OneInstrNpyGenerated': False}, no_cursor_timeout=True):
        path = root_dir + '/' + midi['md5'] + '.mid'
        save_path = npy_file_root_dir + '/' + midi['md5'] + '.npz'

        pm = pretty_midi.PrettyMIDI(path)

        segment_num = pm.get_end_time() / 8
        valid_pieces = int(math.modf(segment_num)[1] + 1) if math.modf(segment_num)[0] >= 0.9 else int(math.modf(segment_num)[1])

        note_range = (24, 108)
        # data = np.zeros((segment_num, 64, 84), np.bool_)
        nonzeros = []
        sixteenth_length = 60 / 120 / 4
        for instr in pm.instruments:
            if not instr.is_drum:
                for note in instr.notes:
                    start = int(note.start / sixteenth_length)
                    end = int(note.end / sixteenth_length)
                    pitch = note.pitch
                    if pitch < note_range[0] or pitch >= note_range[1]:
                        continue
                    else:
                        pitch -= 24
                        for time_raw in range(start, end):
                            segment = int(time_raw / 64)
                            time = time_raw % 64
                            nonzeros.append([segment, time, pitch])

        nonzeros = np.array(nonzeros)
        np.savez_compressed(save_path, nonzeros)

        midi_collection.update_one(
            {'_id': midi['_id']},
            {'$set': {
                'ValidPiecesNum': valid_pieces,
                'PiecesNum': segment_num,
                'OneInstrNpyGenerated': True
            }})

        print('Progress: {:.2%}'.format(
            midi_collection.count({'OneInstrNpyGenerated': True}) / midi_collection.count()))


def build_single_tensor_from_sparse(path):
    midi_collection = get_midi_collection()
    nonzeros = np.load(path)['arr_0']
    midi = midi_collection.find_one({'md5': path[:-4]})
    result = np.zeros((midi['PiecesNum'], 4, 120, 84, 5))
    result[[data for data in nonzeros]] = True
    return result


def build_midi_from_tensor(src_path, save_path, time_step=120, bar_length=4, valid_range=(24, 108)):
    data = build_single_tensor_from_sparse(src_path)
    piece_num = data.shape[0]
    instr_list = ['Drums', 'Piano', 'Guitar', 'Bass', 'Strings']
    program_list = [0, 0, 24, 32, 48]
    pm = pretty_midi.PrettyMIDI()
    for i in range(5):
        instr = instr_list[i]
        is_drum = (instr == 'Drums')
        instr_track = pretty_midi.Instrument(program_list[i], is_drum=is_drum, name=instr)
        track_data = data[:, :, :, :, i]

        for piece in range(piece_num):
            for bar in range(bar_length):
                init_time = piece * (bar_length * time_step) + bar * time_step
                print(init_time)
                for note in range(valid_range[1]-valid_range[0]):

                    during_note = False
                    note_begin = init_time

                    for time in range(time_step):
                        has_note = track_data[piece, bar, time, note]
                        if has_note:
                            if not during_note:
                                during_note = True
                                note_begin = time + init_time
                            else:
                                if time != time_step-1:
                                    continue
                                else:
                                    note_end = time + init_time
                                    print(note_begin / 60, note_end / 60)
                                    instr_track.notes.append(pretty_midi.Note(64, note + 12,
                                                                              note_begin / 48,
                                                                              note_end / 48))
                        else:
                            if not during_note:
                                continue
                            else:
                                note_end = time + init_time
                                print(note_begin / 60, note_end / 60)
                                instr_track.notes.append(pretty_midi.Note(64, note + 12,
                                                                          note_begin / 48,
                                                                          note_end / 48))
                                during_note = False

        pm.instruments.append(instr_track)

    pm.write(save_path)


def generate_nonzeros_by_notes():
    root_dir = 'E:/free_midi_library/scaled_midi/'

    midi_collection = get_midi_collection()
    genre_collection = get_genre_collection()
    for genre in genre_collection.find():
        genre_name = genre['Name']
        print(genre_name)
        npy_file_root_dir = 'E:/midi_matrix/one_instr/' + genre_name + '/'
        if not os.path.exists(npy_file_root_dir):
            os.mkdir(npy_file_root_dir)

        for midi in midi_collection.find({'Genre': genre_name, 'OneInstrNpyGenerated': False}, no_cursor_timeout=True):
            path = root_dir + genre_name + '/' + midi['md5'] + '.mid'
            save_path = npy_file_root_dir + midi['md5'] + '.npz'
            pm = pretty_midi.PrettyMIDI(path)
            segment_num = pm.get_end_time() / 8
            note_range = (24, 108)
            # data = np.zeros((segment_num, 64, 84), np.bool_)
            nonzeros = []
            sixteenth_length = 60 / 120 / 4
            for instr in pm.instruments:
                if not instr.is_drum:
                    for note in instr.notes:
                        start = int(round(note.start / sixteenth_length))
                        end = int(round(note.end / sixteenth_length))
                        pitch = note.pitch
                        if pitch < note_range[0] or pitch >= note_range[1]:
                            continue
                        else:
                            pitch -= 24
                            for time_raw in range(start, end):
                                segment = int(time_raw / 64)
                                time = time_raw % 64
                                print(segment, time, pitch)
                                nonzeros.append([segment, time, pitch])

            nonzeros = np.array(nonzeros)
            np.savez_compressed(save_path, nonzeros)
            midi_collection.update_one({'_id': midi['_id']}, {'$set': {'OneInstrNpyGenerated': True}})
            print('Progress: {:.2%}'.format(
                midi_collection.count({'Genre': genre_name, 'OneInstrNpyGenerated': True}) / midi_collection.count({'Genre': genre_name})), end='\n')


def generate_sparse_matrix_of_genre(genre, phase):
    npy_path = 'D:/data/' + genre + f'/{phase}.npz'
    with np.load(npy_path) as f:
        shape = f['shape']
        data = np.zeros(shape, np.float_)
        nonzeros = f['nonzeros']
        for x in nonzeros:
            data[(int(x[0]), int(x[1]), int(x[2]))] = 1.

    np.random.shuffle(data)
    return data


def generate_sparse_matrix_of_genre_colab(genre, phase):
    npy_path = 'D:/Datasets/steely_data_light/' + genre + f'/{phase}.npz'
    with np.load(npy_path) as f:
        shape = f['shape']
        data = np.zeros(shape, np.float_)
        nonzeros = f['nonzeros']
        for x in nonzeros:
            data[(int(x[0]), int(x[1]), int(x[2]))] = 1.

    np.random.shuffle(data)
    return data


def get_genre_pieces_num(genre):
    genre_collection = get_genre_collection()
    return genre_collection.find_one({'Name': genre})['ValidPiecesNum']


def generate_sparse_matrix_from_multiple_genres(genres):
    length = 0
    genre_collection = get_genre_collection()
    for genre in genre_collection.find({'Name': {'$in': genres}}):
        length += genre['ValidPiecesNum']
    data = np.zeros([length, 64, 84], np.float_)
    for genre in genres:
        npy_path = 'D:/data/' + genre + '/data_sparse.npz'
        with np.load(npy_path) as f:
            nonzeros = f['nonzeros']
            for x in nonzeros:
                data[(x[0], x[1], x[2])] = 1.
    return data


def update_classical_info():
    classical_collection = get_classical_collection()

    genres_collection = get_genre_collection()

    total_valid = 0
    for midi in classical_collection.find():
        total_valid += midi['ValidPiecesNum']

    genres_collection.update_one(
        {'Name': 'classical'},
        {'$set': {
            'PerformersNum': get_classical_composer_collection().count(),
            'ValidPiecesNum': total_valid,
            'TrainPieces': int(total_valid * 0.9),
            'TestPieces': total_valid - int(total_valid * 0.9),
            'FilesNum': get_classical_collection().count()
        }}
    )
    print(total_valid)


def get_latest_lazz():
    jazz_collection = get_jazz_collection()
    valid_pieces = 0
    for midi in jazz_collection.find():
        valid_pieces += midi['ValidPiecesNum']
    print(valid_pieces)
    print(int(valid_pieces * 0.9), valid_pieces - int(valid_pieces * 0.9))


if __name__ == '__main__':
    merge_jazz()