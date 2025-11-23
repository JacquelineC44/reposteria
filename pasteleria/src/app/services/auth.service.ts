import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
<<<<<<< Updated upstream
  private loggedIn = false;

  constructor() {}

  login(username: string, password: string): boolean {
    
    if (username === 'admin' && password === '1234') {
      this.loggedIn = true;
      localStorage.setItem('loggedIn', 'true'); 
=======
  username = "karen";
  password = "1234"
  private isLoggedInStatus = false;
  constructor() { }
  login(username: string, password:string): boolean{
    if (username == this.username && password == this.password ){
      this.isLoggedInStatus = true;
      localStorage.setItem('token','usuario-logueado');
>>>>>>> Stashed changes
      return true;
    }
    return false;
  }

  logout() {
    this.loggedIn = false;
    localStorage.removeItem('loggedIn');
  }

  isLoggedIn(): boolean {
    return this.loggedIn;
  }

