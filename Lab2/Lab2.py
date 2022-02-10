"""Козак А.М. ІП 13
Варіант 17
Створити файл зі списком лікарських ампул: назваб термін дії(ГГ:ХХ), термін зберігання(р). Видалити інформацію про ампули, термін зберігання яких > 1р.
Видати попередження про закінчення терміну зберігання за 10 днів."""

import mod

fileName="medicine list.txt"     #назва списку
print("Input list information: ")
mod.inputFile(fileName)
mod.removeDate(fileName)
print("Edited medicine list: ")
mod.outputFile(fileName)