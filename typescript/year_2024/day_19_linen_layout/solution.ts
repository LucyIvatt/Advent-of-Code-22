import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { substringAtIndex } from '../../utils/misc';

const formatInput = (puzzleInput: string[]) => {
  const input = split2DArray(puzzleInput, '');
  return { towels: input[0][0].split(', '), patterns: input[1] };
};

const findPatternMatches = (puzzleInput: string[], exhaustive = false) => {
  const { towels, patterns } = formatInput(puzzleInput);
  const cache = new Map<string, number>();

  const countMatches = (remainingPattern: string) => {
    if (remainingPattern.length === 0) return 1;

    if (cache.has(remainingPattern)) return cache.get(remainingPattern)!;

    let count = 0;

    for (const towel of towels) {
      if (substringAtIndex(remainingPattern, towel, 0)) {
        const newPattern = remainingPattern.slice(towel.length);
        count += countMatches(newPattern);
        if (!exhaustive && count > 0) break;
      }
    }

    cache.set(remainingPattern, count);
    return count;
  };

  let totalMatches = 0;

  for (const pattern of patterns) {
    const patternMatches = countMatches(pattern);
    totalMatches += patternMatches;
  }

  return totalMatches;
};

export const partOne = (puzzleInput: string[]) => findPatternMatches(puzzleInput).toString();
export const partTwo = (puzzleInput: string[]) => findPatternMatches(puzzleInput, true).toString();

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('19', 'linen_layout', partOne, partTwo, puzzleInput);
}
