import { Observable } from 'rxjs';

export abstract class ServiceGreeter {
	abstract sayHello(helloRequest: HelloRequest): Observable<HelloReply>;
	abstract check(): Observable<void>;
}

export class HelloRequest {
	name: string;
	num: number;
	flag: boolean;

	constructor() {
		this.name = ""
		this.num = null
		this.flag = null
	}
}

export class HelloReply {
	message: string;

	constructor() {
		this.message = ""
	}
}

