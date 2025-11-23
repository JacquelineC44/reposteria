import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service'; // AJUSTA LA RUTA

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  username: string = '';
  password: string = '';
  errorMsg: string = '';

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  login() {

    const ok = this.authService.login(this.username, this.password);

    if (ok) {
      this.router.navigate(['/perfil']);   // ← A donde quieres dirigir después
    } else {
      this.errorMsg = "Usuario o contraseña incorrectos";
    }
  }
}
