import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

type RegexMatch = { match: string; index: number; groups: number[] };

// Matches "mul(x, y)" where x and y are 1-3 digit numbers
const MUL_REGEX = /mul\((\d{1,3}),(\d{1,3})\)/g;

// Matches "do()" or "don't()"
const COND_REGEX = /do\(\)|don't\(\)/g;

const findMatches = (input: string, regex: RegExp): RegexMatch[] => {
  return [...input.matchAll(regex)].map((match) => ({
    match: match[0],
    index: match.index ?? -1,
    groups: match.slice(1).map(Number)
  }));
};

export const partOne = (puzzle_input: string[]) => {
  const instructions = puzzle_input.join('');
  const result = findMatches(instructions, MUL_REGEX).reduce((acc, { groups: [a, b] }) => (acc += a * b), 0);
  return result.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const instructions = puzzle_input.join('');

  const multiplications = findMatches(instructions, MUL_REGEX);
  const conditions = findMatches(instructions, COND_REGEX);

  const result = multiplications.reduce((sum, { groups: [a, b], index }) => {
    const condition = conditions.filter((cond) => cond.index < index).at(-1);

    if (!condition || condition.match === 'do()') {
      sum += a * b;
    }
    return sum;
  }, 0);

  return result.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE_2));
  runPuzzle('03', 'mull_it_over', partOne, partTwo, puzzle_input);
}
