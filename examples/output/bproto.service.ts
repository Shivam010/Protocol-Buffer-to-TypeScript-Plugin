import { Observable } from 'rxjs';
import { Msg } from  './test.service'
import { Emp } from  './Aproto.service'
import { Extra } from  './Aproto.service'

export abstract class Servicecheck {
	abstract use(emp: Emp): Observable<Emp>;
}

export class name {
	id: string;

	constructor() {
		this.id = ""
	}
}

export class full {
	fullName: name;
	ext: Extra;

	constructor() {
		this.fullName = null
		this.ext = null
	}
}

