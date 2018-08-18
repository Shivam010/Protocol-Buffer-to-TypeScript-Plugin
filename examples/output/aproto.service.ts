import { Observable } from 'rxjs';
import { Msg } from  './test.service'

export abstract class ServiceGreeter {
	abstract check(emp: Emp): Observable<Emp>;
}

export class Emp {
	nam: string;
	sam: Msg;

	constructor() {
		this.nam = ""
		this.sam = null
	}
}

export class Extra {
	ext: string;

	constructor() {
		this.ext = ""
	}
}

