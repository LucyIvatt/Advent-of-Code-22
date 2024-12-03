import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const findMatches = (input: string) => {
  const matches = [...input.matchAll(/mul\((\d{1,3}),(\d{1,3})\)/g)];

  return matches.reduce((acc, match) => {
    return (acc += Number(match[1]) * Number(match[2]));
  }, 0);
};

export const partOne = (puzzle_input: string[]) => {
  return puzzle_input.reduce((acc, line) => (acc += findMatches(line)), 0).toString();
};

export const partTwo = (puzzle_input: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('03', 'mull_it_over', partOne, partTwo, puzzle_input);
}
