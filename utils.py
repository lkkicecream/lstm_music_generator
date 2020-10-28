import os
import pickle
import glob

import mido
from mido import Message, MidiFile, MidiTrack
from music21 import converter, instrument, note, chord, stream  # converter负责转换,乐器，音符，和弦类
from music21.chord import Chord
from music21.note import Note

import numpy as np
import generate
import network
import train
import musicTheory as mt
import random

def get_notes():
    """
    从music_midi目录中的所有MIDI文件里读取note，chord
    Note样例：B4，chord样例[C3,E4,G5],多个note的集合，统称“note”
    """
    notes = []
    for midi_file in glob.glob("music_midi/*.mid"):
        # 读取music_midi文件夹中所有的mid文件,file表示每一个文件
        stream = converter.parse(midi_file)  # midi文件的读取，解析，输出stream的流类型

        # 获取所有的乐器部分，开始测试的都是单轨的
        parts = instrument.partitionByInstrument(stream)
        if parts:  # 如果有乐器部分，取第一个乐器部分
            notes_to_parse = parts.parts[0].recurse()  # 递归
        else:
            notes_to_parse = stream.flat.notes  # 纯音符组成
        for element in notes_to_parse:  # notes本身不是字符串类型
            # 如果是note类型，取它的音高(pitch)
            if isinstance(element, note.Note):
                # 格式例如：E6
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                # 转换后格式：45.21.78(midi_number)
                notes.append('.'.join(str(n) for n in element.normalOrder))  # 用.来分隔，把n按整数排序
    # 如果 data 目录不存在，创建此目录
    if not os.path.exists("data"):
        os.mkdir("data")
    # 将数据写入data/notes
    with open('data/notes', 'wb') as filepath:  # 从路径中打开文件，写入
        pickle.dump(notes, filepath)  # 把notes写入到文件中
    return notes  # 返回提取出来的notes列表


def create_music(prediction, count='weights-99'):  # 生成音乐函数，训练不用
    """ 用神经网络预测的音乐数据来生成mid文件 """
    offset = 0  # 偏移，防止数据覆盖
    output_notes_1 = []
    output_notes_2 = []
    mid = MidiFile()
    track = MidiTrack()
    #track2 = MidiTrack()
    mid.tracks.append(track)
    #mid.tracks.append(track2)

    '''
    這裡生成的效果感覺適合節奏樂器
    # 生成Note或chord对象
    for data in prediction:

        beats = random.randint(0,16)
        rythem = mt.combineRythem(beats)

        for note_lenght in rythem:
            # 如果是chord格式：45.21.78
            if ('.' in data) or data.isdigit():  # data中有.或者有数字
                note_in_chord = data.split('.')  # 用.分隔和弦中的每个音
                notes = []  # notes列表接收单音
                for current_note in note_in_chord:
                    new_note = note.Note(int(current_note))  # 把当前音符化成整数，在对应midi_number转换成note
                    new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
                    notes.append(new_note)
                new_chord = chord.Chord(notes)  # 再把notes中的音化成新的和弦
                new_chord.offset = offset  # 初试定的偏移给和弦的偏移
                output_notes_1.append(new_chord)  # 把转化好的和弦传到output_notes中
            # 是note格式：
            else:
                new_note = note.Note(data)  # note直接可以把data变成新的note
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
                output_notes_1.append(new_note)  # 把new_note传到output_notes中
            # 每次迭代都将偏移增加，防止交叠覆盖
            offset += note_lenght
    '''

    '''# 旋律未添加 rhythm'''
    for data in prediction:
        # 如果是chord格式：45.21.78
        if ('.' in data) or data.isdigit():  # data中有.或者有数字
            note_in_chord = data.split('.')  # 用.分隔和弦中的每个音
            notes = []  # notes列表接收单音
            for current_note in note_in_chord:
                new_note = note.Note(int(current_note))  # 把当前音符化成整数，在对应midi_number转换成note
                new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
                notes.append(new_note)
            new_chord = chord.Chord(notes)  # 再把notes中的音化成新的和弦
            new_chord.offset = offset  # 初试定的偏移给和弦的偏移
            output_notes_1.append(new_chord)  # 把转化好的和弦传到output_notes中
        # 是note格式：
        else:
            new_note = note.Note(data)  # note直接可以把data变成新的note
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
            output_notes_1.append(new_note)  # 把new_note传到output_notes中
        # 每次迭代都将偏移增加，防止交叠覆盖
        offset += 0.5

    # 创建音乐流(stream)
    midi_stream = stream.Stream(output_notes_1)  # 把上面的循环输出结果传到流
    # 写入midi文件
    midi_stream.write('midi', fp='./beethoven_output/output_original' + count +'.mid')  # 最终输出的文件名是output.mid，格式是mid

    '''旋律添加 rhythm'''
    beats = []
    rythem = []
    index = 0
    output_notes_1 = []
    
    for data in prediction:
        if index == len(rythem):
            beats = random.randint(1,17)
            rythem = mt.combineRhythm(beats)
            index = 0

        note_lenght = rythem[index]
        index += 1
        # 如果是chord格式：45.21.78
        if ('.' in data) or data.isdigit():  # data中有.或者有数字
            note_in_chord = data.split('.')  # 用.分隔和弦中的每个音
            notes = []  # notes列表接收单音
            for current_note in note_in_chord:
                new_note = note.Note(int(current_note))  # 把当前音符化成整数，在对应midi_number转换成note
                new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
                notes.append(new_note)
            new_chord = chord.Chord(notes)  # 再把notes中的音化成新的和弦
            new_chord.offset = offset  # 初试定的偏移给和弦的偏移
            output_notes_1.append(new_chord)  # 把转化好的和弦传到output_notes中
        # 是note格式：
        else:
            new_note = note.Note(data)  # note直接可以把data变成新的note
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()  # 乐器用钢琴
            output_notes_1.append(new_note)  # 把new_note传到output_notes中
        # 每次迭代都将偏移增加，防止交叠覆盖
        offset += note_lenght

    # 创建音乐流(stream)
    midi_stream = stream.Stream(output_notes_1)  # 把上面的循环输出结果传到流
    # 写入midi文件
    midi_stream.write('midi', fp='./beethoven_output/output_add_rythem' + count +'.mid')  # 最终输出的文件名是output.mid，格式是mid

# 新增引數 note_Number
def produce_notes(model, network_input, pitch_names, num_pitch, note_Number=100):
    # 从输入里随机选择一个序列，作为生成的音乐的起始点
    start = np.random.randint(0, len(network_input) - 1)
 
    # 创建一个字典，用于映射 整数 和 音调
    int_to_pitch = dict((num, pitch) for num, pitch in enumerate(pitch_names))
 
    pattern = network_input[start]
 
    # 神经网络实际生成的音调
    prediction_output = []
 
    # 生成 700 个 音符/音调
    for note_index in range(note_Number):
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        # 输入 归一化
        prediction_input = prediction_input / float(num_pitch)
 
        # 用载入了训练所得最佳参数文件的神经网络来 预测/生成 新的音调
        prediction = model.predict(prediction_input, verbose=0)
 
        # argmax 取最大的那个维度（类似 One-Hot 独热码）
        index = np.argmax(prediction)
 
        # 将 整数 转成 音调
        result = int_to_pitch[index]
 
        prediction_output.append(result)
 
        # 往后移动1个单位
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    return prediction_output

# 加载用于训练神经网络的音乐数据
def produce(weights='best'):

    # 打開最佳的訓練結果或是選擇使用的檔案
    hdf5_file = ""
    if weights == 'best':
        hdf5_file = glob.glob('./beethoven_weight/*.hdf5')[-1]
    else:
        hdf5_file = glob.glob(f'./beethoven_weight/*-{weights}-*.hdf5')[0]
    print(hdf5_file)

    with open('data/notes', 'rb') as filepath:
        notes = pickle.load(filepath)
    # 得到所有音调的名字
    pitch_names = sorted(set(item for item in notes))
    # 得到所有不重复（因为用了set）的音调数目
    num_pitch = len(set(notes))

    network_input, normalized_input = generate.prepare_sequences(notes, pitch_names, num_pitch)
    # 载入之前训练时最好的参数文件（最好用 loss 最小 的那一个参数文件，
    # 记得要把它的名字改成 best-weights.hdf5 ），来生成神经网络模型cl
    model = network.network_model(normalized_input, num_pitch, hdf5_file)

    # 用神经网络来生成音乐数据
    prediction = produce_notes(model, network_input, pitch_names, num_pitch, 400)

    # 用预测的音乐数据生成 MIDI 文件，再转换成 MP3
    create_music(prediction)


if __name__ == '__main__':
    produce()
