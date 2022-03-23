#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# self is a reference to an object

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
