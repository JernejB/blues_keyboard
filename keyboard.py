import pygame, fluidsynth
from pygame.locals import *

import fluidsynth

# Pro scale generator
def pitch(tone):
    return [tone,tone+3,tone+5,tone+6,tone+7,tone+10,tone+11,tone+12]

# TODO: plays a chord with root note. More options (in list?)?
# settings = [major, minor, sept] 
def play_chord(start, fs, rNote, pitch=0, settings=[0,0,0]):
    rNote = rNote + pitch
    chord = [rNote, rNote+7]
    if settings[0]:
        chord.insert(1,rNote+4)
    elif settings[1]: chord.insert(1,rNote+3)
    elif settings[2]: chord.append(rNote+10)
    if start:
        for note in chord:
            fs.noteon(0, note, 127)
    else:
        for note in chord:
            fs.noteoff(0,note)    



# FluidSynt init
fs = fluidsynth.Synth(0.2,48000)
fs.start('alsa')
# Set instrument
inst = fs.sfload("/home/jernej/Documents/Python/keyboard/yamahagrandpiano44.sf2")

fs.program_select(0, inst, 0, 0)

# Pygame init
pygame.display.set_mode((1,1))
pygame.init()

running = True
# WIP
bTone = pitch(50)
mTone = pitch(50+12)
hTone = pitch(50+24)
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #print event
            if event.key == K_a:
                play_chord(1, fs, bTone[0])
                #fs.noteon(0, bTone[0], 127)
                #fs.noteon(0, bTone[0]+7, 127)

            if event.key == K_q:
                fs.noteon(0, bTone[0], 127)
                fs.noteon(0, bTone[0]+4, 127)
                fs.noteon(0, bTone[0]+7, 127)

            if event.key == K_s:
                fs.noteon(0, bTone[0]+5, 127)
                fs.noteon(0, bTone[0]+12, 127)
                
            if event.key == K_d:
                fs.noteon(0, bTone[0]+7, 127)
                fs.noteon(0, bTone[0]+14, 127)
                 
            if event.key == K_r:
                fs.noteon(0, bTone[0]+8, 127)
                fs.noteon(0, bTone[0]+15, 127)
                
            if event.key == K_f:
                fs.noteon(0, mTone[4], 127)
                
            if event.key == K_g:
                fs.noteon(0, mTone[0], 100)
            if event.key == K_h:
                fs.noteon(0, mTone[1], 127)
            if event.key == K_j:
                fs.noteon(0, mTone[2], 127)
            if event.key == K_k:
                fs.noteon(0, mTone[3], 127)
            if event.key == K_l:
                fs.noteon(0, mTone[4], 127)
            if event.key == 232:
                fs.noteon(0, mTone[5], 127)
            if event.key == 230:
                fs.noteon(0, mTone[6], 127)
            if event.key == 190:
                fs.noteon(0, mTone[7], 127)
                

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(1)
                running = False

                
        elif event.type == KEYUP:
            
            if event.key == K_a:
                play_chord(0, fs, bTone[0])
                #fs.noteoff(0, bTone[0])
                #fs.noteoff(0, bTone[0]+7)

            if event.key == K_q:
                fs.noteoff(0, bTone[0])
                fs.noteoff(0, bTone[0]+4)
                fs.noteoff(0, bTone[0]+7)
                
            if event.key == K_s:
                fs.noteoff(0, bTone[0]+5)
                fs.noteoff(0, bTone[0]+12)
                
            if event.key == K_d:
                fs.noteoff(0, bTone[0]+7)
                fs.noteoff(0, bTone[0]+14)
            if event.key == K_r:
                fs.noteoff(0, bTone[0]+8)
                fs.noteoff(0, bTone[0]+15)
            
            if event.key == K_f:
                fs.noteoff(0, mTone[4])
            if event.key == K_g:
                fs.noteoff(0, mTone[0])
            if event.key == K_h:
                fs.noteoff(0, mTone[1])
            if event.key == K_j:
                fs.noteoff(0, mTone[2])
            if event.key == K_k:
                fs.noteoff(0, mTone[3])
            if event.key == K_l:
                fs.noteoff(0, mTone[4])
            if event.key == 232:
                fs.noteoff(0, mTone[5])
            if event.key == 230:
                fs.noteoff(0, mTone[6])
            if event.key == 190:
                fs.noteoff(0, mTone[7])
           


