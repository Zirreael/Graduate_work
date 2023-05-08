import cv2     # модуль openCV
import numpy


def viewImage(image, name_of_window):   # функция отображения изображения в отдельном окне
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)    # ожидает нажатия любой клавиши, после чего окно с изображением закрывается
    cv2.destroyAllWindows()


def resizeImage(image, percent):    # функция изменения размера изображения на заданный процент
    width = int(image.shape[1] * percent / 100)
    height = int(image.shape[0] * percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    win_name = "window resize"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.imshow(win_name, resized)
    cv2.resizeWindow(win_name, width, height)
    cv2.waitKey(0)     # ожидает нажатия любой клавиши, после чего окно с изображением закрывается


def get_information(image):     # первая часть курсовой, вынесенная в отдельную функцию
    viewImage(image, "window")
    lab_l_channel = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)     # перевод изображения в канал с яркостью
    width = int(image.shape[1])
    height = int(image.shape[0])
    x = int(input(f"\nВведите координату x пикселя в диапазоне от 0 до {width - 1}: "))
    y = int(input(f"Введите координату y пикселя в диапазоне от 0 до {height - 1}: "))
    (b, g, r) = image[y, x]
    print("\nКрасный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    (l, a, b) = lab_l_channel[y, x]
    print("\nЯркость заданного пикселя = ", l)


def clustering(image):     # функция кластеризации
    claster = []     # список кластеров
    lab_l_channel = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)     # перевод изображения в канал с яркостью
    for i in range(256):
        claster.append([])      # на каждое значение яркости (от 0 до 255) создает отдельный кластер
    width = int(image.shape[1])
    height = int(image.shape[0])
    for i in range(height):
        for j in range(width):
            (l, a, b) = lab_l_channel[i, j]     # получение яркости одного пикселя
            claster[l].append([i, j])     # занесение пикселя в соответствующий кластер
    n = 10      # границы диапазона
    m = 25
    for j in range(n, m+1):     # закраска определенного диапазона кластеров красным цветом для наглядности
        lenght = len(claster[j])
        for i in range(lenght):
            [x, y] = claster[j][i]
            image[x, y] = (0, 0, 255)
    resizeImage(image, 50)      # изменение размера изображение и вывод результата на экран


if __name__ == '__main__':
    img = cv2.imread('image.tif', cv2.IMREAD_COLOR)
    print("Кластеризация выполняется, пожалуйста ожидайте...")
    clustering(img)  
