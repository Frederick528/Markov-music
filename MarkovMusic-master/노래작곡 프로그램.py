import pysynth as ps
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
from src.MarkovMusic import MusicMatrix

def make_midi(midi_path, notes, Accompaniment = None, bpm=85, tracks_number=1):
    note_names = 'c c# d d# e f f# g g# a a# b'.split()

    result1 = NoteSeq()
    for n in notes:
        duration = 1. / n[1]

        if n[0].lower() == 'r':
            result1.append(Rest(dur=duration))
        else:
            pitch = n[0][:-1]
            octave = int(n[0][-1]) + 1
            pitch_number1 = note_names.index(pitch.lower())
            
            result1.append(Note(pitch_number1, octave=octave, dur=duration))
    result2 = NoteSeq()
    if Accompaniment != None:
        for n in Accompaniment:
            duration = 1. / n[1]

            if n[0].lower() == 'r':
                result2.append(Rest(dur=duration))
            else:
                pitch = n[0][:-1]
                octave = int(n[0][-1]) + 1
                pitch_number2 = note_names.index(pitch.lower())
                
                result2.append(Note(pitch_number2, octave=octave, dur=duration))
            
    midi = Midi(number_tracks=tracks_number, tempo=bpm)
    midi.seq_notes(result1, track=0)
    if tracks_number == 2:
        midi.seq_notes(result2, track=1)
    midi.write(midi_path)
# 음표 숫자 계산법 a + ··· + b + ··· + c → (a*c)/(a + ··· + b + ··· + c) (단, 가장 작거나 큰 값은 a와 C여야 함.)    예시) 점4분음표 = 4 + 8 → (4*8)/(4+8) = 8/3
# #[32 16(반의 반박) 8(반박) 4(1박) 2(2박) 1(4박) 1/2] / [점8분음표 8+16 = 16+16+16 → 16/3], [점4분음표 4+8 → 8/3], [점2분음표2+4 → 4/3], [점온음표 1+2 → 2/3], [2+16 → 16/9], [점점4분음표 4 + 8 + 16 → 16/7]

# somebody khaim
# song1 = [['g4', 8], ['d5', 16], ['c5', 8], ['a#4', 16/3], ['a4', 8], ['a#4', 8], ['a4', 8], ['f4', 16], ['g4', 16/5], ['r', 32], ['r', 32], ['g4', 32], ['a4', 16], ['g4', 16], ['a#4', 16], ['c5', 16], ['a#4', 16], ['a4', 16/3], ['f4', 16], ['d4', 41/18], ['c4', 16], ['d4', 16], ['f4', 4], ['d#4', 8], ['d4', 8/3]]
# song2 = [['r', 32], ['r', 32], ['g4', 32], ['a4', 16], ['g4', 16], ['a#4', 16], ['g4', 16], ['c5', 16], ['a4', 16], ['d5', 16], ['d#5', 16], ['f5', 8], ['d5', 16/3], ['g4', 16/3], ['r', 16], ['r', 32], ['r', 32], ['f4', 64], ['f#4', 64], ['g4', 16], ['a4', 16], ['a#4', 8], ['c5', 8], ['a#4', 16], ['g5', 8], ['a#5', 16], ['c6', 8]]
# song3 = [['r', 32], ['r', 32], ['c5', 32], ['a#4', 32], ['g4', 32], ['f4', 32], ['d4', 32], ['f4', 64], ['f#4', 64], ['g4', 64], ['d5', 41/18], ['g4', 8], ['d5', 16], ['c5', 8], ['a#4', 16/3], ['a4', 8], ['a#4', 8], ['a4', 8], ['f4', 16], ['g4', 16/5], ['r', 4], ['f5', 2]]
# song = song1 + song2 + song3

song1 = [['r', 8], ['e5', 8], ['d5', 8], ['c5', 8], ['c5', 8], ['b4', 8], ['a#4', 8], ['b4', 8], ['d5', 8], ['c5', 8], ['b4', 8], ['c5', 8], ['g5', 8/3], ['f5', 8], ['e5', 8/3], ['d5', 8], ['d5', 8/3], ['c5', 8], ['d5', 2], ['e5', 8/3], ['e4', 8]]
song2 = [['c5', 8/3], ['e4', 8], ['b4', 8/3], ['e4', 8], ['a4', 4], ['g4', 8], ['f4', 8], ['g4', 8/3], ['c4', 8], ['d4', 8], ['f4', 8], ['a4', 8], ['c5', 8], ['b4', 8], ['g4', 8], ['e4', 8], ['d4', 8], ['e4', 4/3], ['r', 8], ['e4', 8]]
song3 = [['c5', 8/3], ['e4', 8], ['b4', 8/3], ['e4', 8], ['a4', 4], ['g4', 8], ['f4', 8], ['g4', 8/3], ['e4', 8], ['d4', 8], ['f4', 8], ['a4', 8], ['c5', 8], ['d5', 8], ['e5', 8], ['b4', 8], ['g4', 8], ['a4', 2], ['f3', 8], ['e3', 8], ['d3', 8], ['e3', 8]]
song4 = [['c4', 8/3], ['e3', 8], ['b3', 8/3], ['e3', 8], ['a3', 4], ['g3', 8], ['f3', 8], ['g3', 8/3], ['c3', 8], ['d3', 8], ['f3', 8], ['a3', 8], ['c4', 8], ['b3', 8], ['g3', 8], ['e3', 8], ['d3', 8], ['e3', 4/3], ['r', 8], ['e3', 8]]
song = song1 + song2 + song3 + song4
ACP1 = [['d3', 8], ['f3', 8], ['a3', 8], ['c4', 8/5], ['e3', 8], ['g3', 8], ['c4', 4], ['f3', 8], ['a3', 8], ['c4', 4], ['f#3', 8], ['a3', 8], ['c4', 4/3], ['g3', 8], ['c4', 8], ['d4', 4], ['g#3', 2]]
ACP2 = [['a2', 8], ['e3', 8], ['a3', 4], ['g2', 8], ['e3', 8], ['g3', 4], ['f2', 8], ['c3', 8], ['f3', 4], ['e2', 8], ['c3', 8], ['e3', 4], ['d2', 8], ['a2', 8], ['c3', 4], ['g2', 8], ['d3', 8], ['f3', 4], ['c3', 8], ['e3', 8], ['g3', 8], ['b3', 8], ['g#3', 8], ['a3', 8], ['b3', 4]]
ACP3 = [['a2', 8], ['e3', 8], ['a3', 4], ['g2', 8], ['e3', 8], ['g3', 4], ['f2', 8], ['c3', 8], ['f3', 4], ['e2', 8], ['c3', 8], ['e3', 4], ['d2', 8], ['a2', 8], ['d3', 4], ['e2', 8], ['b2', 8], ['e3', 4], ['a2', 8], ['e3', 8], ['d3', 8], ['e3', 8], ['r', 2]]
ACP4 = [['a1', 8], ['e2', 8], ['a2', 4], ['g1', 8], ['e2', 8], ['g2', 4], ['f1', 8], ['c2', 8], ['f2', 4], ['e1', 8], ['c2', 8], ['e2', 4], ['d2', 4], ['f2', 4], ['g2', 4], ['d2', 4], ['c2', 8], ['e2', 8], ['g2', 8], ['b2', 8], ['g#2', 8], ['a2', 8], ['b2', 4]]
ACP = ACP1 + ACP2 + ACP3 + ACP4


ps.make_wav(song, bpm = 85, fn='examples/실험1.wav')
ps.make_wav(ACP1, bpm = 85, fn='examples/실험2.wav')
ps.mix_files('examples/실험1.wav', 'examples/실험2.wav', 'examples/실험3.wav') #1과 2를 합쳐 3으로
 
make_midi(midi_path='midi/테스트.mid', notes=song, Accompaniment=ACP, bpm = 106, tracks_number=2)

# 마르코프 체인을 이용하여 새로운 곡을 제작하는 코드↓

# matrix = MusicMatrix(song)

# start_note = ['e5', 8]

# random_song = []
# random_song.append(start_note)
# for i in range(0, 80):
#     start_note = matrix.next_note(start_note)
#     random_song.append(start_note)

# matrix2 = MusicMatrix(ACP)

# start_note2 = ['f3', 8]

# random_ACP = []
# random_ACP.append(start_note2)
# for j in range(0, 80):
#     start_note2 = matrix2.next_note(start_note2)
#     random_ACP.append(start_note2)

# ps.make_wav(random_song, fn='examples/random.wav')
# ps.make_wav(song, bpm = 135, fn='midi/실험.wav')

# make_midi(midi_path='midi/작곡3.mid', notes=random_song, Accompaniment=random_ACP, bpm = 106, tracks_number=2)
