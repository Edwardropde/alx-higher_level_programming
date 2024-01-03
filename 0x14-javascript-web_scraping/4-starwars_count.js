#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
	const parsed = JSON.parse(body).results;
	if (error) console.log(error);

	let appearances = 0;
	for (let i = 0; i < parsed.length; i++) {
		for (let j = 0; j < parsed[i].characters.length; j++) {
			if (parsed[i].characters[j].match('18')) {
				appearances++;
			}
		}
	}
	console.log(appearances);
});
