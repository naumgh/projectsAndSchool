import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComputerWinsComponent } from './computer-wins.component';

describe('ComputerWinsComponent', () => {
  let component: ComputerWinsComponent;
  let fixture: ComponentFixture<ComputerWinsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComputerWinsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComputerWinsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
