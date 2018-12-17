import { Observable } from 'rxjs';
import { Msg } from  './test.service'

export abstract class ServiceGreeter {
	abstract check(emp: Emp): Observable<Emp>;
	abstract boolCheck(boolValue: boolean): Observable<boolean>;
}

export class Emp {
	nam: string;
	sam: Msg;

	constructor() {
		this.nam = null;
		this.sam = new Msg();
	}
}

export class Extra {
	ext: string;

	constructor() {
		this.ext = null;
	}
}

