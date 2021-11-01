function findPairs(A){
	let i = 0;
	let j = A.length-1;
	
	while(i < j)
	{
		if(A[i] + A[j] === sum){
			console.log("Found the pairs!");
			console.log("[",A[i],",",A[j],"]");

			break;
		}

		if(A[i] + A[j] < sum){
			i++;
		}

		if(A[i] + A[j] > sum){
			j--;
		}

		if(i === j){
			console.log("No pairs found!");
		}
	
	}
}

A = [2,2,6,7];
B = [1,2,4,4];
C = [1,2,3,4];
D = [1,4,6,9];
E = [0,1,6,7];

let sum = 8;

findPairs(E);
