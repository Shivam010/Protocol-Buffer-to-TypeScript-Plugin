import { Observable } from 'rxjs';
import {Extra} from  './aproto.service'
import {Emp} from  './aproto.service'
import {Msg} from  './test.service'

export abstract class Servicecheck {
	abstract use(emp: Emp): Observable<Emp>;
}

export interface name {
	id: string;
}

export interface full {
	fullName: name;
	ext: Extra;
}

