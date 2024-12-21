import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { MinPriorityQueue } from '@datastructures-js/priority-queue';

type Match = { towel: string; currentString: string };

const substringAtStart = (str: string, subStr: string): boolean => {
  return str.slice(0, subStr.length) === subStr;
};

const formatInput = (puzzleInput: string[]) => {
  const input = split2DArray(puzzleInput, '');
  return { towels: input[0][0].split(', '), patterns: input[1] };
};

const findPatternMatches = (puzzleInput: string[], exhaustive = false) => {
  const { towels, patterns } = formatInput(puzzleInput);
  let validPatterns = 0;

  for (const pattern of patterns) {
    const pq = new MinPriorityQueue<Match>((match) => match.currentString.length);

    towels.forEach((towel) => {
      if (substringAtStart(pattern, towel)) pq.enqueue({ towel, currentString: pattern });
    });

    while (!pq.isEmpty()) {
      const { towel, currentString } = pq.dequeue()!;
      const newPattern = currentString.slice(towel.length);

      if (newPattern.length === 0) {
        validPatterns++;
        if (!exhaustive) break;
      } else {
        towels.forEach((towel) => {
          if (substringAtStart(newPattern, towel)) pq.enqueue({ towel, currentString: newPattern });
        });
      }
    }
  }
  return validPatterns.toString();
};

export const partOne = (puzzleInput: string[]) => findPatternMatches(puzzleInput);

export const partTwo = (puzzleInput: string[]) => findPatternMatches(puzzleInput, true);

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('19', 'linen_layout', partOne, partTwo, puzzleInput);
}
