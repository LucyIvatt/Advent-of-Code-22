import { readFileSync } from 'fs';

export enum InputFile {
  EXAMPLE = 'example.txt',
  EXAMPLE_2 = 'example2.txt',
  INPUT = 'input.txt'
}

/**
 * Reads the content of a puzzle input file, splits it into lines, trims each line,
 * and filters out any empty lines.
 *
 * @param fileName - The name of the file to read.
 * @returns An array of non-empty, trimmed lines from the file.
 */
export const readPuzzleInput = (fileName: string): string[] => {
  return readFileSync(fileName, 'utf-8')
    .split('\n')
    .map((line) => line.trim());
};

export const split2DArray = (puzzleInput: string[], delimiter: string): string[][] => {
  return puzzleInput.reduce(
    (acc, curr) => {
      if (curr === delimiter) {
        acc.push([]);
      } else {
        acc[acc.length - 1].push(curr);
      }
      return acc;
    },
    [[]] as string[][]
  );
};
