'''
    Проект-форк https://github.com/FahadulShadhin/Sorting-Algorithms-Visualizer
'''

from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort
from algorithms.stalinSort import stalin_sort


# Main window 
window = Tk()
window.title("Визуализация алгоритмов сортировки")
window.maxsize(1000, 700)
window.config(bg = WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Сортировка пузырьком', 'Сортировка вставками', 'Сортировка выбором', 'Сортировка слиянием', 'Быстрая сортировка', 'Пирамидальная сортировка', 'Подсчетом', 'Сталин']
speed_list = ['Медленно', 'Средне', 'Быстро']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == speed_list[0]:
        return 0.3
    elif speed_menu.get() == speed_list[1]:
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == algo_list[0]:
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == algo_list[1]:
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == algo_list[2]:
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == algo_list[3]:
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == algo_list[4]:
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == algo_list[5]:
        heap_sort(data, drawData, timeTick)
    elif algo_menu.get() == algo_list[6]:
        counting_sort(data, drawData, timeTick)
    elif algo_menu.get() == algo_list[7]:
        stalin_sort(data, drawData, timeTick)


### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Алгоритм: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Скорость: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Отсортировать", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Сгенерировать массив", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)


window.mainloop()
