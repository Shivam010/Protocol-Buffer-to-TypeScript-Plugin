import { Observable } from 'rxjs';

export abstract class ServiceGreeter {
	abstract check(emp: Emp): Observable<Emp>;
}

export interface Emp {
	nam: string;
}

