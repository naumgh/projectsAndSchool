import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProjectDto } from '../services/project.dto';
import { ProjectService } from '../services/project.service';
import { SharedDataService } from '../shared-data.service';

// interface Project {
//   id: number;
//   title: string;
//   description: string;
//   status: string;
// }

@Component({
  selector: 'app-projects-page',
  templateUrl: './projects-page.component.html',
  styleUrls: ['./projects-page.component.css']
})
export class ProjectsPageComponent implements OnInit {
  // admin status
  isAdmin: boolean = false;

  // Modal Bools
  showCreateProjectModal = false;
  showEditProjectModal = false;

  // Create Project Fields
  newProjectForm!: FormGroup
  editProjectForm!: FormGroup

  teamId!: number;
  teamName!: string;
  projects: ProjectDto[] = [];
  companyId!: number;
  selectedProjectToEdit?: ProjectDto;
  activeDropdownOpen = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private fb: FormBuilder,
    private projectService: ProjectService,
    private sharedDataService: SharedDataService
  ) { }

  ngOnInit() {
    // Initialize fields for team projects to display
    const queryParams = this.route.snapshot.queryParamMap;
    this.teamId = +(queryParams.get('id') || 0);
    this.teamName = queryParams.get('name') || 'Unknown Team';
    this.companyId = +(queryParams.get('companyId') || 0);

    // Subscribe to isAdmin
    this.sharedDataService.isAdmin$.subscribe((adminstatus) => {
      this.isAdmin = adminstatus;
    });

    // Initialize fields for creating projects
    this.newProjectForm = this.fb.group({
      projectName: ['', Validators.required],
      description: ['', Validators.required]
    });

    this.editProjectForm = this.fb.group({
      projectName: ['', Validators.required],
      description: ['', Validators.required],
      active: [true, Validators.required]
    })

    // Load Projects
    this.loadProjects(this.companyId, this.teamId);
  }

  loadProjects(companyId: number, teamId: number) {

    this.projectService.getProjectsByTeamId(companyId, teamId).subscribe({
      next: (data) => {
        this.projects = data;
      },
      error: (err) => {
        console.error('Failed to load projects: ', err);
      }
    })

  }

  goBackToTeams() {
    this.router.navigate(['teams']);
  }

  // Create Project Modal Methods
  openCreateProjectModal() {
    this.showCreateProjectModal = true;
  }

  closeCreateProjectModal() {
    this.showCreateProjectModal = false;
  }

  submitNewProject() {
    // Check for valid new project form before creatingnew project
    if (this.newProjectForm.valid) {
      const newProject: ProjectDto = {
        name: this.newProjectForm.value.projectName,
        description: this.newProjectForm.value.description,
        active: true
      };

      this.projectService.postProjectToTeam(this.teamId, newProject).subscribe({
        next: (createdProject) => {
          this.projects.push(createdProject);
          this.closeCreateProjectModal();
          this.newProjectForm.reset();
        },
        error: (err) => {
          console.error('Failed to create project: ', err);
        }
      });
    }
  }

  submitEditProject() {
    if (this.selectedProjectToEdit && this.editProjectForm.valid) {
      const updatedProject: ProjectDto = {
        ...this.selectedProjectToEdit,
        name: this.editProjectForm.value.projectName,
        description: this.editProjectForm.value.description,
        active: this.editProjectForm.value.active
      };

      console.log('Submitting updated project:', updatedProject);

      this.projectService.patchProjectToTeam(this.teamId, updatedProject).subscribe({
        next: (updated: ProjectDto) => {
          console.log('Project updated from backend:', updated);

          const index = this.projects.findIndex(p => p.id === updated.id);
          if (index > -1) {
            this.projects[index] = updated;
          }

          this.loadProjects(this.companyId, this.teamId);
          this.closeEditProjectModal();
        },
        error: (err) => {
          console.error('Failed to update project: ', err);
        }
      });
    }
  }

  // Edit Project Modal Methods
  openEditProjectModal(project: ProjectDto) {
    this.selectedProjectToEdit = { ...project };
    this.editProjectForm.setValue({
      projectName: project.name,
      description: project.description,
      active: project.active ?? true
    });

    this.showEditProjectModal = true;
  }

  closeEditProjectModal() {
    this.showEditProjectModal = false;
  }

  toggleActiveDropdown() {
    this.activeDropdownOpen = !this.activeDropdownOpen;
  }

  selectActive(value: boolean) {
    this.editProjectForm.patchValue({ active: value });
    this.activeDropdownOpen = false;
  }

}
