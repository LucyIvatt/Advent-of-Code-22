import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

class IndexRange {
  value: number;
  left: number;
  right: number;

  constructor(id: number, left: number, right: number) {
    this.value = id;
    this.left = left;
    this.right = right;
  }

  getLength = () => this.right - this.left + 1;
  toString = () => `{value:${this.value}, range:[${this.left}, ${this.right}], length:${this.getLength()}}`;
  updateRange = (left: number, right: number) => {
    this.left = left;
    this.right = right;
  };
}

const checkSum = (blocks: IndexRange[]) => {
  return blocks.reduce((checkSum, block) => {
    for (let i = block.left; i <= block.right; i++) {
      checkSum += block.value * i;
    }
    return checkSum;
  }, 0);
};

const findBlocks = (puzzleInput: string[]): IndexRange[] => {
  let currentIndex = 0;
  const blocks: IndexRange[] = [];
  const values = puzzleInput[0].split('').map(Number);

  for (let i = 0; i < values.length; i++) {
    if (i % 2 === 0) blocks.push(new IndexRange(i / 2, currentIndex, currentIndex + values[i] - 1));
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

const shuffleSingleChars = (blocks: IndexRange[]) => {
  let i = 0;

  while (i < blocks.length - 1) {
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
        gap.updateRange(0, -1); // Empty gap
      } else {
        gap.left += lastBlock.getLength();
        blocks.pop();
      }

      blocks.splice(insertPosition, 0, newBlock);
      insertPosition++;
    }

    i++;
  }

  return blocks;
};

const shuffleEntireFiles = (blocks: IndexRange[]) => {
  const gaps = findGaps(blocks);

  for (const block of blocks.sort((a, b) => b.value - a.value)) {
    for (let j = 0; j < gaps.length; j++) {
      const gap = gaps[j];
      if (gap.getLength() >= block.getLength() && gap.left < block.left) {
        const blockLength = block.getLength();
        block.right = gap.left + blockLength - 1;
        block.left = gap.left;

        gap.left = gap.left + blockLength;

        if (gap.left > gap.right) {
          gaps.splice(j, 1);
        }
        break;
      }
    }
  }

  return blocks;
};

export const partOne = (puzzleInput: string[]) => {
  const formatted = findBlocks(puzzleInput);
  const blocks = shuffleSingleChars(formatted);
  return checkSum(blocks).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const formatted = findBlocks(puzzleInput);
  const blocks = shuffleEntireFiles(formatted);
  return checkSum(blocks).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
