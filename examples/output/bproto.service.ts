import { Observable } from 'rxjs';
import { MetadataEntry } from  './Bproto.full.service'
import { Msg } from  './test.service'
import { Emp } from  './Aproto.service'
import { Extra } from  './Aproto.service'

export abstract class Servicecheck {
	abstract use(emp: Emp): Observable<Emp>;
}

export class name {
	id: string;

	constructor() {
		this.id = "";
	}
}

export class full {
	fullName: name;
	ext: Extra;
	friends: name[];
	metadata: {
		[key: string]: number;
	};
	birthDate: string;

	constructor() {
		this.fullName = new name();
		this.ext = new Extra();
		this.friends = [];
		this.metadata = {};
		this.birthDate = "";
	}
}

