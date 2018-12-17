import { Observable } from 'rxjs';
import { Msg } from  './test.service'
import { Emp } from  './Aproto.service'
import { Extra } from  './Aproto.service'

export abstract class ServiceCheck {
	abstract use(emp: Emp): Observable<Emp>;
}

export class Name {
	id: string;

	constructor() {
		this.id = null;
	}
}

export class Full {
	fullName: Name;
	ext: Extra;
	friends: Name[];
	metadata: {
		[key: string]: number;
	};
	birthDate: string;

	constructor() {
		this.fullName = new Name();
		this.ext = new Extra();
		this.friends = [];
		this.metadata = {};
		this.birthDate = "";
	}
}

