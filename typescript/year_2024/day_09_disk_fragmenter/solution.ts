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

const shuffle = (blocks: FileBlock[]) => {
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

export const partOne = async (puzzleInput: string[]) => {
  const formatted = formatInput(puzzleInput);
  const blocks = shuffle(formatted);

  console.log(blocks);

  let checkSum = 0;

  for (const block of blocks) {
    for (let i = block.range[0]; i <= block.range[1]; i++) {
      checkSum += block.id * i;
    }
  }

  return checkSum.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('09', 'disk_fragmenter', partOne, partTwo, puzzleInput);
}
