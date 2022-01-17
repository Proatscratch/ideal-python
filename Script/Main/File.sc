Script Main: gen{
	var hello = "Hello, World";
	function Hello: Void{
		out(hello);
		out(self);
		
	}
	Hello();
};

run{<Main>};
//Hello, World
//<Main value=[{"hello":"Hello, World","Hello":["void",[print(hel
//lo),print(self)]],'Hello()'}] Type = "Gen">
gen.out.global()
out{Main}
//<Main value=[{"hello":"Hello, World","Hello":["void",[print(hel
//lo),print(self)]],'Hello()'}] Type = "Gen">
out{Gen}
//<gen value=[Hidden] Type = "python.packet">

