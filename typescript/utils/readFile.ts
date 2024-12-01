import { readFileSync } from 'fs';

export enum InputFile {
  EXAMPLE = 'example.txt',
  INPUT = 'input.txt'
}

export const readPuzzleInput = (fileName: string): string[] => {
  return readFileSync(fileName, 'utf-8')
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
};
