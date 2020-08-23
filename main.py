import random

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
screen.fill((255, 255, 255))
running = True
array = []


def main():
    global running
    makeArray()
    while running:
        screen.fill([0, 0, 0])
        draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("quicksort")
                    quickSort(array, 0, screen.get_width() - 1)

                if event.key == pygame.K_b:
                    print("bubblesort")
                    bubbleSort()
                if event.key == pygame.K_e:
                    running = False

                if event.key == pygame.K_r:
                    print("reset")
                    makeArray()

    pygame.quit()


def makeArray():
    global screen, array
    array = []
    for i in range(0, screen.get_width()):
        value = []
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        value.append([r, g, b])
        value.append(r+g+b)
        array.append(value)


def draw():
    global screen, array
    for i in range(0, screen.get_width()):
        pygame.draw.line(screen, (array[i][0][0], array[i][0][1], array[i][0][2]),
                         (i, screen.get_height()), (i, screen.get_height() - array[i][1]))

    pygame.display.update()


def bubbleSort():
    global array
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j][1] > array[j + 1][1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break
        screen.fill([0, 0, 0])
        draw()
        pygame.display.update()


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high][1]

    for j in range(low, high):

        if arr[j][1] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    screen.fill([0, 0, 0])
    draw()
    pygame.display.update()
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


main()
