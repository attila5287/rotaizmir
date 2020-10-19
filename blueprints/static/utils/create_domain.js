const create_domain = (d, i) => {
	if (i == 0) {
		return ["turquoise", "aqua", d.slice(i, i + 2)].flat();
	} else if (i == 1) {
		return ["turqoise", d.slice(i - 1, i + 2)].flat();
	} else {
		return d.slice(i - 2, i + 2);
	}
};
