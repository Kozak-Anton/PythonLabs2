"""Козак А.М. ІП 13
Варіант 17
Створити текстовий файл. Переписати його компоненти до нового текстового файлу, вставляючи на початку рядка порядковий номер,
в кінці рядка - поточну довжину рядка у вихідному файлі. Вивести вміст вихідного і створеного файлів."""

import mod

initFile = "initText.txt" #початковий файл
editFile = "editText.txt" #відредагований файл

print("Input initial text here(Enter empty line or Ctrl+Z for end of input): ")
mod.inputFile(initFile)
mod.rewriteFile(initFile, editFile)
print("Initial text: ")
mod.outputFile(initFile)
print("Edited text: ")
mod.outputFile(editFile)
