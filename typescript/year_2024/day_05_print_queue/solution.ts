import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { count } from '../../utils/misc';

const formatInputs = (puzzle_input: string[]) => {
  const delimiterIndex = puzzle_input.indexOf('');

  const rules = puzzle_input.slice(0, delimiterIndex).map((rule) => rule.split('|').map(Number));
  const lists = puzzle_input.slice(delimiterIndex + 1).map((list) => list.split(',').map(Number));

  return { rules, lists };
};

const getValidRules = (list: number[], rules: number[][]): number[][] => {
  const set = new Set(list);
  return rules.filter(([a, b]) => set.has(a) && set.has(b));
};

const processLists = (lists: number[][], rules: number[][], fixBrokenOrders = false): number => {
  let totalSum = 0;

  for (const list of lists) {
    const validRules = getValidRules(list, rules);
    const counts = count(validRules.map(([, b]) => b));

    const isValid = list.every((item, i) => counts[item] === i || (!counts[item] && i === 0));

    if (!fixBrokenOrders && isValid) totalSum += list[Math.floor(list.length / 2)];

    if (fixBrokenOrders && !isValid) {
      list.sort((a, b) => (counts[a] || 0) - (counts[b] || 0));
      totalSum += list[Math.floor(list.length / 2)];
    }
  }

  return totalSum;
};

export const partOne = (puzzle_input: string[]) => {
  const { rules, lists } = formatInputs(puzzle_input);
  return processLists(lists, rules).toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const { rules, lists } = formatInputs(puzzle_input);
  return processLists(lists, rules, true).toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('05', 'print_queue', partOne, partTwo, puzzle_input);
}
