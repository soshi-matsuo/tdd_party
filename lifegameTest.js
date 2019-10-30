'use strict';
const lifegame = require('./lifegame.js');
require('./config.js');

describe('Game of Life', () => {
	it('judge underpopulation', () => {
		let board = '..*.....' +
					'....*...' +
					'...**...' +
					'........';
		let cellIdx = 2;
		global.expect(lifegame.willDie(cellIdx, board)).to.equal(true);
	});
	it('judge overpopulation', () => {
		let board = '..*.*...' +
					'....**..' +
					'...**...' +
					'........';
		let cellIdx = 12;
		global.expect(lifegame.willDie(cellIdx, board)).to.equal(true);
	});
	it('judge alive', () => {
		let board = '..*.....' +
					'....*...' +
					'...**...' +
					'........';
		let cellIdx = 12;
		global.expect(lifegame.willDie(cellIdx, board)).to.equal(false);
	});
	it('judge willDie to dead cell', () => {
		let board = '..*.....' +
					'....*...' +
					'...**...' +
					'........';
		let cellIdx = 31;
		global.expect(lifegame.willDie(cellIdx, board)).to.equal(false);
	});
	it('judge give birth', () => {
		let board = '........' +
					'....*...' +
					'...**...' +
					'........';
		let cellIdx = 11;
		global.expect(lifegame.givingBirth(cellIdx, board)).to.equal(true);
	});
	it('generate next board', () => {
		let board = '........' +
					'....*...' +
					'...**...' +
					'........';
		let expectedBoard = '........' +
							'...**...' +
							'...**...' +
							'........';
		global.expect(lifegame.generateBoard(board)).to.equal(expectedBoard);
	});
	it('generate greatgrandson', () => {
		let board = '........' +
					'....*...' +
					'...**...' +
					'........';
		let greatgrandson = '........' +
							'...**...' +
							'...**...' +
							'........';
		global.expect(lifegame.play(board, 3)).to.equal(greatgrandson);
	});
});
