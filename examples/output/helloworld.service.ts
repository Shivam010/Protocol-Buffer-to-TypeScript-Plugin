import { Observable } from 'rxjs';

export abstract class ServiceGreeter {
	abstract sayHello(helloRequest: HelloRequest): Observable<HelloReply>;
	abstract check(): Observable<void>;
}

export interface HelloRequest {
	name: string;
	num: number;
	flag: boolean;
}

export interface HelloReply {
	message: string;
}

