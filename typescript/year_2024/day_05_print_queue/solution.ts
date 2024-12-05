import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { count } from '../../utils/misc';

export const partOne = (puzzle_input: string[]) => {
  const delimiterIndex = puzzle_input.indexOf('');

  const orderingRules = puzzle_input.slice(0, delimiterIndex).map((rule) => rule.split('|').map(Number));
  const lists = puzzle_input.slice(delimiterIndex + 1).map((list) => list.split(',').map(Number));

  let sum = 0;

  for (const list of lists) {
    const validRules = orderingRules.filter(([a, b]) => list.includes(a) && list.includes(b));
    const counts = count(validRules.map(([, b]) => b));

    if (
      list.every((item, i) => {
        return counts[item] === i || (!counts[item] && i === 0);
      })
    ) {
      sum += list[Math.floor(list.length / 2)];
    }
  }

  return sum.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const delimiterIndex = puzzle_input.indexOf('');

  const orderingRules = puzzle_input.slice(0, delimiterIndex).map((rule) => rule.split('|').map(Number));
  const lists = puzzle_input.slice(delimiterIndex + 1).map((list) => list.split(',').map(Number));

  let sum = 0;

  for (const list of lists) {
    const validRules = orderingRules.filter(([a, b]) => list.includes(a) && list.includes(b));
    const counts = count(validRules.map(([, b]) => b));

    if (
      !list.every((item, i) => {
        return counts[item] === i || (!counts[item] && i === 0);
      })
    ) {
      list.sort((a, b) => (counts[a] || 0) - (counts[b] || 0));
      sum += list[Math.floor(list.length / 2)];
    }
  }

  return sum.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('05', 'print_queue', partOne, partTwo, puzzle_input);
}
