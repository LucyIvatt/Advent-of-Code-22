import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord } from '../../utils/grid';

export type FileBlock = { id: number; range: [number, number]; length: number };

const formatInput = (puzzleInput: string[]) => {
  const blocks: FileBlock[] = [];
  let currentIndex = 0;

  puzzleInput[0].split('').forEach((val, index) => {
    if (index % 2 === 0) {
      blocks.push({ id: index / 2, range: [currentIndex, currentIndex + Number(val) - 1], length: Number(val) });
    }
    currentIndex += Number(val);
  });
  return blocks;
};

const shuffleSingleChars = (blocks: FileBlock[]) => {
  let i = 0;

  while (i < blocks.length - 2) {
    const b1 = blocks[i];
    const b2 = blocks[i + 1];

    let gapLength = b2.range[0] - b1.range[1] - 1;
    let gapLocation = b1.range[1] + 1;

    let newBlockPos = i + 1;

    while (gapLength != 0) {
      const lastBlock = blocks.at(-1);
      if (!lastBlock) throw new Error('no final element found');

      const lastBlockLength = lastBlock.range[1] - lastBlock.range[0] + 1;

      let newBlock;

      if (lastBlockLength > gapLength) {
        // last block bigger than the gap, will remain in the list
        newBlock = { id: lastBlock.id, range: [gapLocation, gapLocation + gapLength - 1] as Coord, length: gapLength };
        lastBlock.range = [lastBlock.range[0], lastBlock.range[1] - gapLength];
        gapLength = 0;
      } else {
        // last block smaller than the gap, will be removed
        newBlock = {
          id: lastBlock.id,
          range: [gapLocation, gapLocation + lastBlockLength - 1] as Coord,
          length: lastBlockLength
        };
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

  last.range = [last_2.range[1] + 1, last_2.range[1] + last.range[1] - last.range[0] + 1];

  return blocks;
};

const shuffleEntireFiles = (blocks: FileBlock[]) => {
  console.log(blocks);
  // Find all possible gaps
  const gaps = [];
  let i = 0;
  while (i < blocks.length - 1) {
    const leftBound = blocks[i].range[1];
    const rightBound = blocks[i + 1].range[0];
    if (leftBound + 1 !== rightBound)
      gaps.push({ range: [leftBound + 1, rightBound - 1], length: rightBound - 1 - leftBound });
    i++;
  }

  for (const block of blocks.sort((a, b) => b.id - a.id)) {
    console.log('processing', block);
    for (let j = 0; j < gaps.length; j++) {
      const gap = gaps[j];
      if (gap.length >= block.length && gap.range[0] < block.range[0]) {
        console.log('found gap', gap);
        block.range = [gap.range[0], gap.range[0] + block.length - 1];

        gap.range = [gap.range[0] + block.length, gap.range[1]];
        gap.length = gap.length - block.length;

        console.log(block);
        console.log(gap);

        if (gap.range[0] > gap.range[1]) {
          console.log('removing gap', gap);
          gaps.splice(j, 1);
        }
        console.log('\n');
        break;
      }
    }
  }

  console.log(blocks);

  return blocks;
};

export const partOne = async (puzzleInput: string[]) => {
  const formatted = formatInput(puzzleInput);
  const blocks = shuffleSingleChars(formatted);

  let checkSum = 0;

  for (const block of blocks) {
    for (let i = block.range[0]; i <= block.range[1]; i++) {
      checkSum += block.id * i;
    }
  }

  return checkSum.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const formatted = formatInput(puzzleInput);
  const blocks = shuffleEntireFiles(formatted);

  let checkSum = 0;

  for (const block of blocks) {
    for (let i = block.range[0]; i <= block.range[1]; i++) {
      checkSum += block.id * i;
    }
  }

  return checkSum.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
