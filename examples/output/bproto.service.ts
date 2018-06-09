import { Observable } from 'rxjs';
import * as Aproto from './aproto.service'

export abstract class Servicecheck {
	abstract use(emp: Aproto.Emp): Observable<Aproto.Emp>;
}

export interface name {
	id: string;
}

export interface full {
	fullName: name;
}

