import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginPageComponent } from './login-page/login-page.component';
import { SelectCompanyPageComponent } from './select-company-page/select-company-page.component';
import { AnnouncementsPageComponent } from './announcements-page/announcements-page.component';
import { ProjectsPageComponent } from './projects-page/projects-page.component';
import { TeamsPageComponent } from './teams-page/teams-page.component';
import { UsersPageComponent } from './users-page/users-page.component';

const routes: Routes = [
  { path: '', component: LoginPageComponent },
  { path: 'select-company', component: SelectCompanyPageComponent },
  { path: 'announcements', component: AnnouncementsPageComponent },
  { path: 'teams', component: TeamsPageComponent },
  { path: 'projects', component: ProjectsPageComponent },
  { path: 'users', component: UsersPageComponent, runGuardsAndResolvers: 'always' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
