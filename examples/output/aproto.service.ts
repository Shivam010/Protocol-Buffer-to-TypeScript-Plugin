import { Observable } from 'rxjs';
import { Msg } from  './test.service'

export abstract class ServiceGreeter {
	abstract check(emp: Emp): Observable<Emp>;
}

export interface Emp {
	nam: string;
	sam: Msg;
}

export interface Extra {
	ext: string;
}

