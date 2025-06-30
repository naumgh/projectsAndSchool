import { Component, EventEmitter, Input, Output } from '@angular/core';
import { BasicUserDto } from 'src/app/services/basic-user.dto';
import { TeamDto } from 'src/app/services/team.service';

@Component({
  selector: 'app-teams-card',
  templateUrl: './teams-card.component.html',
  styleUrls: ['./teams-card.component.css']
})
export class TeamsCardComponent {
  @Input() team!: TeamDto;
  @Output() clicked = new EventEmitter<void>();

  onCardClick() {
    this.clicked.emit();
  }

  getMemberName(user: BasicUserDto): string {
    return `${user.profile.firstName} ${user.profile.lastName}`;
  }

}
