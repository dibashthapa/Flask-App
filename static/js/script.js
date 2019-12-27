function follow(e){
	if (e.textContent=='Follow'){
		e.textContent='Following'
		console.log(document.getElementsByTagName('span').length);
	}
	else{
		e.textContent="Follow"
	}
}