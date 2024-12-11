import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const shiftStone = (stone: number): number[] => {
  if (stone == 0) return [1];

  const stoneString = stone.toString();
  const length = stoneString.length;

  return length % 2 === 0
    ? [Number(stoneString.substring(0, length / 2)), Number(stoneString.substring(length / 2))]
    : [stone * 2024];
};

const processBlinks = (stones: number[], blinks: number) => {
  let stoneCounts = new Map<number, number>();
  stones.forEach((s) => stoneCounts.set(s, 1));

  for (let i = 0; i < blinks; i++) {
    const updatedStones = new Map<number, number>();
    for (const [s, num] of stoneCounts) {
      stoneCounts.delete(s);

      const newStones = shiftStone(s);

      for (const x of newStones) updatedStones.set(x, (updatedStones.get(x) ?? 0) + num);
    }
    stoneCounts = updatedStones;
  }

  let ans = 0;
  for (const count of stoneCounts.values()) ans += count;

  return ans.toString();
};

export const partOne = (puzzleInput: string[]) => {
  const stones = puzzleInput[0].split(' ').map(Number);
  return processBlinks(stones, 25);
};

export const partTwo = (puzzleInput: string[]) => {
  const stones = puzzleInput[0].split(' ').map(Number);
  return processBlinks(stones, 75);
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('11', 'plutonian_pebbles', partOne, partTwo, puzzleInput);
}
