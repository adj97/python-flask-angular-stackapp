import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  apioutput: object = [null];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  getapioutput(){
    this.http.get(window.location.protocol + '//' + window.location.hostname + ':' + 5001 + '/really/very/long/api/route')
      .subscribe((res: object) => {
        this.apioutput = res["msg" as keyof Object];
        console.log(res)});
  }

}
