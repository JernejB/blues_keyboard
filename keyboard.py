#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, fluidsynth
from pygame.locals import *

import fluidsynth

# Pro scale generator
def generate_scale(tone):
    return [tone,tone+3,tone+5,tone+6,tone+7,tone+10,tone+11,tone+12]


def play_chord(start, fs, rNote, settings = {'major':0, 'minor':0, '7':0}, pitch = 0):
    rNote = rNote + pitch
    chord = [rNote, rNote+7]
    if settings['major']:
        chord.insert(1,rNote+4)
    if settings['minor']: chord.insert(1,rNote+3)
    if settings['7']: chord.append(rNote+10)
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
inst = fs.sfload("yamahagrandpiano44.sf2")

fs.program_select(0, inst, 0, 0)

# Pygame init
pygame.display.set_mode((1,1))
pygame.init()

running = True
# WIP
bTone = generate_scale(50)    # Bass
mTone = generate_scale(50+12) # Mid
hTone = generate_scale(50+24) # High
chord_settings = {'major':0, 'minor':0, '7':0}

# True = Chords; False = Walking Bass
chord_walking = True

## Key bindings

## A,S,D,F = chords; default: root + fifth
## Q,W,E,R = major
## Y,X,C,V = minor
## SHIFT   = seventh chord modifier?
#  A ... I
#  S ... IV
#  D ... V
#  F ... uhh...chord that falls down to dominant?

## G-Ž = blues scale
#  Z ... Supertonic
#  U ... Mediant
#  O ... Submediant flat?



while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            
            print event
            # Play chords
            if event.key == 49:
                chord_walking = True
            # Play Walking Bass Progression
            if event.key == 50:
                chord_walking = False
            # Seventh modifier
            if event.key == 304:
                chord_settings['7'] = not chord_settings['7']

            # Major chords
            if event.key == K_q:
                chord_settings['major']=1
                play_chord(1,fs,bTone[0],chord_settings)
                chord_settings['major']=0
                
            if event.key == K_w:
                chord_settings['major']=1
                play_chord(1,fs,bTone[2],chord_settings)
                chord_settings['major']=0
            if event.key == K_e:
                chord_settings['major']=1
                play_chord(1,fs,bTone[4],chord_settings)
                chord_settings['major']=0
            if event.key == K_r:
                chord_settings['major']=1
                play_chord(1,fs,bTone[4]+1,chord_settings)
                chord_settings['major']=0


            # Root + Fifth Chords
            if event.key == K_a: play_chord(1, fs, bTone[0], chord_settings)
            if event.key == K_s: play_chord(1, fs, bTone[2], chord_settings)
            if event.key == K_d: play_chord(1, fs, bTone[4], chord_settings)
            if event.key == K_f: play_chord(1, fs, bTone[4]+1,chord_settings)

            # Minor Chords and Walking Bass
            if event.key == 60 and not chord_walking: # key: <
                fs.noteon(0, bTone[0],127)

            if event.key == K_y:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(1,fs,bTone[0],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteon(0, bTone[1]+1, 127)

            if event.key == K_x:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(1,fs,bTone[2],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteon(0, bTone[4], 127)                
            if event.key == K_c:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(1,fs,bTone[4],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteon(0, bTone[4]+2, 127)
            if event.key == K_v:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(1,fs,bTone[4]+1,chord_settings)
                    chord_settings['minor']=0
                else: fs.noteon(0,bTone[5],127)
            # Scale
            if event.key == K_g: fs.noteon(0, mTone[0], 127)
            if event.key == K_z: fs.noteon(0, mTone[1]-1, 127)
            if event.key == K_h: fs.noteon(0, mTone[1], 127)
            if event.key == K_u: fs.noteon(0, mTone[1]+1, 127)
            if event.key == K_j: fs.noteon(0, mTone[2], 127)
            if event.key == K_k: fs.noteon(0, mTone[3], 127)
            if event.key == K_l: fs.noteon(0, mTone[4], 127)
            if event.key == K_p: fs.noteon(0, mTone[4]+1, 127)
            if event.key == 232: fs.noteon(0, mTone[5], 127)
            if event.key == 230: fs.noteon(0, mTone[6], 127)
            if event.key == 190: fs.noteon(0, mTone[7], 127)
                
            ## QUIT
            if event.key == K_ESCAPE:
                pygame.quit()
                running = False

                
        elif event.type == KEYUP:
            # Major Chords
            if event.key == K_q:
                chord_settings['major']=1
                play_chord(0,fs,bTone[0],chord_settings)
                chord_settings['major']=0
            if event.key == K_w:
                chord_settings['major']=1
                play_chord(0,fs,bTone[2],chord_settings)
                chord_settings['major']=0
            if event.key == K_e:
                chord_settings['major']=1
                play_chord(0,fs,bTone[4],chord_settings)
                chord_settings['major']=0
            if event.key == K_r:
                chord_settings['major']=1
                play_chord(0,fs,bTone[4]+1,chord_settings)
                chord_settings['major']=0
            # Root + Fifth Chords
            if event.key == K_a: play_chord(0, fs, bTone[0], chord_settings)    
            if event.key == K_s: play_chord(0, fs, bTone[2], chord_settings)
            if event.key == K_d: play_chord(0, fs, bTone[4], chord_settings)
            if event.key == K_f: play_chord(0, fs, bTone[4]+1,chord_settings)
            # Minor Chords and walking bass
            if event.key == 60 and not chord_walking: # key: <
                fs.noteoff(0, bTone[0])
            if event.key == K_y:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(0,fs,bTone[0],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteoff(0, bTone[1]+1)
            if event.key == K_x:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(0,fs,bTone[2],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteoff(0, bTone[4])
            if event.key == K_c:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(0,fs,bTone[4],chord_settings)
                    chord_settings['minor']=0
                else: fs.noteoff(0, bTone[4]+2)
            if event.key == K_v:
                if chord_walking:
                    chord_settings['minor']=1
                    play_chord(0,fs,bTone[4]+1,chord_settings)
                    chord_settings['minor']=0
                else: fs.noteoff(0, bTone[5])

            # Scale
            if event.key == K_g: fs.noteoff(0, mTone[0])
            if event.key == K_z: fs.noteoff(0, mTone[1]-1)
            if event.key == K_h: fs.noteoff(0, mTone[1])
            if event.key == K_u: fs.noteoff(0, mTone[1]+1)
            if event.key == K_j: fs.noteoff(0, mTone[2])
            if event.key == K_k: fs.noteoff(0, mTone[3])
            if event.key == K_l: fs.noteoff(0, mTone[4])
            if event.key == K_p: fs.noteoff(0, mTone[4]+1)
            if event.key == 232: fs.noteoff(0, mTone[5])
            if event.key == 230: fs.noteoff(0, mTone[6])
            if event.key == 190: fs.noteoff(0, mTone[7])
           


