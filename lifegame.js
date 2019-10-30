'use strict';

module.exports = {
	willDie,
	givingBirth,
	generateBoard,
	play
};

function isAlive(cell) {
	return cell === "*";
}

function getNeighbors(cellIdx, board) {
	let up = board[cellIdx-8];
	let down = board[cellIdx+8];
	let right = board[cellIdx+1];
	let left = board[cellIdx-1];
	let upRight = board[cellIdx-8+1];
	let upLeft = board[cellIdx-8-1];
	let downRight = board[cellIdx+8+1];
	let downLeft = board[cellIdx+8-1];

	let neighbors = [up, down, right, left, upRight, upLeft, downRight, downLeft];

	return neighbors;
}

function countLiveCells(neighbors) {
	let countLiveCell = 0;
	neighbors.forEach((neighbor)=> {
		if(neighbor === '*') {
		countLiveCell++;
		}
	});

	return countLiveCell;
}

function willDie(cellIdx, board) {
	if(!isAlive(board[cellIdx])) {
		return false;
	}
	
	const countLiveCell = countLiveCells(getNeighbors(cellIdx, board));

	if (countLiveCell === 2 || countLiveCell === 3){
		return false;
	}

	return true;
}

function givingBirth(cellIdx, board){
	if(isAlive(board[cellIdx])) {
		return false;
	}
	
	const countLiveCell = countLiveCells(getNeighbors(cellIdx, board));

	if(countLiveCell === 3){
		return true;
	}

	return false;
}

function generateBoard(board) {
	let nextBoard = '';

	for (let i=0; i < board.length; i++) {
		if(willDie(i, board)){
			nextBoard += '.';
			continue;
		} 
		
		if(givingBirth(i, board)){
			nextBoard += '*';
			continue;
		}

		nextBoard += board[i];
	}

	return nextBoard;
}

function play(board, num){

	let result = [];

	result.push(board);

	for(let i=0; i < num; i++){
		result.push(generateBoard(result[result.length - 1]));
	}

	return result[result.length -1];
}