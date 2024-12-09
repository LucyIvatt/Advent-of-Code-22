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
}

const checkSum = (blocks: IndexRange[]) => {
  return blocks.reduce((checkSum, block) => {
    for (let i = block.left; i <= block.right; i++) {
      checkSum += block.value * i;
    }
    return checkSum;
  }, 0);
};

const formatInput = (puzzleInput: string[]) => {
  const blocks: IndexRange[] = [];
  let currentIndex = 0;

  puzzleInput[0].split('').forEach((val, index) => {
    if (index % 2 === 0) {
      blocks.push(new IndexRange(index / 2, currentIndex, currentIndex + Number(val) - 1));
    }
    currentIndex += Number(val);
  });

  return blocks;
};

const shuffleSingleChars = (blocks: IndexRange[]) => {
  let i = 0;

  while (i < blocks.length - 2) {
    const b1 = blocks[i];
    const b2 = blocks[i + 1];

    let gapLength = b2.left - b1.right - 1;
    let gapLocation = b1.right + 1;

    let newBlockPos = i + 1;

    while (gapLength != 0) {
      const lastBlock = blocks.at(-1);
      if (!lastBlock) throw new Error('no final element found');

      const lastBlockLength = lastBlock.getLength();

      let newBlock;

      if (lastBlockLength > gapLength) {
        // last block bigger than the gap, will remain in the list
        newBlock = new IndexRange(lastBlock.value, gapLocation, gapLocation + gapLength - 1);
        lastBlock.right = lastBlock.right - gapLength;
        gapLength = 0;
      } else {
        // last block smaller than the gap, will be removed
        newBlock = new IndexRange(lastBlock.value, gapLocation, gapLocation + lastBlockLength - 1);
        gapLength -= lastBlockLength;
        gapLocation += lastBlockLength;
        blocks.pop();
      }

      blocks.splice(newBlockPos, 0, newBlock);
      newBlockPos++;
    }
    i += gapLength === 0 ? 1 : 2;
  }

  const last = blocks.at(-1);
  const last_2 = blocks.at(-2);

  if (!last || !last_2) throw new Error("Can't find final 2 elements");
  const lastLength = last.getLength(); // need to define this or length is off due to change in left first

  last.left = last_2.right + 1;
  last.right = last.left + lastLength - 1;

  return blocks;
};

const shuffleEntireFiles = (blocks: IndexRange[]) => {
  // Find all possible gaps
  const gaps: IndexRange[] = [];
  let i = 0;
  while (i < blocks.length - 1) {
    const leftBound = blocks[i].right;
    const rightBound = blocks[i + 1].left;
    const gap = new IndexRange(0, leftBound + 1, rightBound - 1);
    if (leftBound + 1 !== rightBound) gaps.push(gap);
    i++;
  }

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
  const formatted = formatInput(puzzleInput);
  const blocks = shuffleSingleChars(formatted);
  return checkSum(blocks).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const formatted = formatInput(puzzleInput);
  const blocks = shuffleEntireFiles(formatted);
  return checkSum(blocks).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
