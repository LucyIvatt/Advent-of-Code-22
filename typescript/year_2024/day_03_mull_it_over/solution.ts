import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

type RegexMatch = { match: string; index: number; groups: number[] };

const MUL_REGEX = /mul\((\d{1,3}),(\d{1,3})\)/g;
const COND_REGEX = /do\(\)|don't\(\)/g;

const findMatches = (input: string, re: RegExp): RegexMatch[] => {
  return [...input.matchAll(re)].map((match) => ({
    match: match[0],
    index: match.index ?? 0,
    groups: match.slice(1).map(Number)
  }));
};

export const partOne = (puzzle_input: string[]) => {
  const instructions = puzzle_input.join('');

  return findMatches(instructions, MUL_REGEX)
    .reduce((acc, match) => (acc += match.groups[0] * match.groups[1]), 0)
    .toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const instructions = puzzle_input.join('');

  const mul_instructions = findMatches(instructions, MUL_REGEX);
  const cond_instructions = findMatches(instructions, COND_REGEX);

  return mul_instructions
    .reduce((acc, instruction) => {
      const earlierConditions = cond_instructions.filter((a) => a.index < instruction.index);
      const conditional = earlierConditions[earlierConditions.length - 1];

      if (!conditional || conditional.match === 'do()') {
        return (acc += instruction.groups[0] * instruction.groups[1]);
      }

      return acc;
    }, 0)
    .toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('03', 'mull_it_over', partOne, partTwo, puzzle_input);
}
