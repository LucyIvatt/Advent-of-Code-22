import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { IndexRange } from '../../utils/range';

const checkSum = (blocks: IndexRange[]) => {
  return blocks.reduce((sum, block) => {
    for (let i = block.left; i <= block.right; i++) {
      sum += block.value * i;
    }
    return sum;
  }, 0);
};

const parseBlocks = (puzzleInput: string[]): IndexRange[] => {
  let currentIndex = 0;
  const blocks: IndexRange[] = [];
  const values = puzzleInput[0].split('').map(Number);

  for (let i = 0; i < values.length; i++) {
    if (i % 2 === 0) {
      blocks.push(new IndexRange(i / 2, currentIndex, currentIndex + values[i] - 1));
    }
    currentIndex += values[i];
  }
  return blocks;
};

const findGaps = (blocks: IndexRange[]): IndexRange[] =>
  blocks
    .slice(0, -1)
    .flatMap((block, i) =>
      block.right + 1 < blocks[i + 1].left ? [new IndexRange(0, block.right + 1, blocks[i + 1].left - 1)] : []
    );

/**
 * Reorganises blocks to fill gaps, shuffling single characters.
 */
const shuffleSingleChars = (blocks: IndexRange[]) => {
  for (let i = 0; i < blocks.length - 1; i++) {
    const leftBlock = blocks[i];
    const rightBlock = blocks[i + 1];
    const gap = new IndexRange(0, leftBlock.right + 1, rightBlock.left - 1);

    let insertPosition = i + 1;

    while (gap.getLength() > 0) {
      const lastBlock = blocks.at(-1)!;
      const isLastBlockLarger = lastBlock.getLength() > gap.getLength();

      const newBlock = isLastBlockLarger
        ? new IndexRange(lastBlock.value, gap.left, gap.right)
        : new IndexRange(lastBlock.value, gap.left, gap.left + lastBlock.getLength() - 1);

      if (isLastBlockLarger) {
        lastBlock.right -= gap.getLength();
        gap.left = gap.right + 1; // mark gap as empty
      } else {
        gap.left += lastBlock.getLength();
        blocks.pop();
      }

      blocks.splice(insertPosition++, 0, newBlock);
    }
  }

  return blocks;
};

/**
 * Reorganises blocks to fill gaps by shuffling entire blocks.
 */
const shuffleEntireFiles = (blocks: IndexRange[]) => {
  const gaps = findGaps(blocks);

  for (let i = blocks.length - 1; i >= 0; i--) {
    const block = blocks[i];

    for (let j = 0; j < gaps.length; j++) {
      const gap = gaps[j];

      if (gap.getLength() >= block.getLength() && gap.left < block.left) {
        block.updateRange(gap.left, gap.left + block.getLength() - 1);
        gap.left = gap.left + block.getLength();

        if (gap.left > gap.right) gaps.splice(j, 1); // removes gap if now empty
        break;
      }
    }
  }

  return blocks;
};

export const partOne = (puzzleInput: string[]) => {
  return checkSum(shuffleSingleChars(parseBlocks(puzzleInput))).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return checkSum(shuffleEntireFiles(parseBlocks(puzzleInput))).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
