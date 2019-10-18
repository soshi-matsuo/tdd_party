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
	it('judge give birth', () => {
		let board = '........' +
					'....*...' +
					'...**...' +
					'........';
		let cellIdx = 11;
		global.expect(lifegame.givingBirth(cellIdx, board)).to.equal(true);
	});
});
