import { Observable } from 'rxjs';
import { Msg } from  './test.service'
import { Emp } from  './Aproto.service'
import { Extra } from  './Aproto.service'

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

