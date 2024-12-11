import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const shiftStone = (stone: number): number[] => {
  if (stone === 0) return [1];

  const stoneString = stone.toString();
  const length = stoneString.length;

  if (length % 2 === 0) {
    const half = length / 2;
    return [Number(stoneString.substring(0, half)), Number(stoneString.substring(half))];
  }

  return [stone * 2024];
};

const processBlinks = (stones: number[], blinks: number) => {
  const stoneCounts = new Map<number, number>();

  stones.forEach((stone) => {
    stoneCounts.set(stone, (stoneCounts.get(stone) ?? 0) + 1);
  });

  for (let i = 0; i < blinks; i++) {
    const currentStones = new Map<number, number>(stoneCounts);
    stoneCounts.clear();
    for (const [stone, count] of currentStones) {
      const newStones = shiftStone(stone);

      for (const newStone of newStones) stoneCounts.set(newStone, (stoneCounts.get(newStone) ?? 0) + count);
    }
  }

  return Array.from(stoneCounts.values())
    .reduce((sum, count) => sum + count, 0)
    .toString();
};

export const partOne = (puzzleInput: string[]) => {
  return processBlinks(puzzleInput[0].split(' ').map(Number), 25);
};

export const partTwo = (puzzleInput: string[]) => {
  return processBlinks(puzzleInput[0].split(' ').map(Number), 75);
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('11', 'plutonian_pebbles', partOne, partTwo, puzzleInput);
}
